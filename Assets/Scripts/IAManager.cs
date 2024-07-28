using System.Collections;
using TMPro;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.Networking;
using UnityEngine.UI;

public class IAManager : MonoBehaviour
{
    public OnResponseEvent OnResponse;

    [System.Serializable]
    public class OnResponseEvent : UnityEvent<string> { }

    private string apiUrl = "http://127.0.0.1:5000/ask";

    public TextMeshProUGUI textArea;

    public void AskChatBot(string question)
    {
        if (string.IsNullOrEmpty(question))
        {
            Debug.LogWarning("La pregunta no puede estar vacía.");
            return;
        }

        Debug.Log("Enviando mensaje al bot: " + question);
        StartCoroutine(SendRequest(question));
    }
    private IEnumerator SendRequest(string message)
    {
        WWWForm form = new WWWForm();
        form.AddField("question", message);
        Debug.Log("Mensaje formateado para el servidor: " + message);

        using (UnityWebRequest www = UnityWebRequest.Post(apiUrl, form))
        {
            www.timeout = 10;

            yield return www.SendWebRequest();

            if (www.result == UnityWebRequest.Result.Success)
            {
                Debug.Log("Respuesta del servidor: " + www.downloadHandler.text);

                string jsonResponse = www.downloadHandler.text;

                try
                {
                    var response = JsonUtility.FromJson<ChatResponse>(jsonResponse);
                    Debug.Log("Respuesta del bot: " + response.reply);
                    OnResponse.Invoke(response.reply);
                }
                catch (System.Exception e)
                {
                    Debug.LogError("Error al parsear la respuesta JSON: " + e.Message);
                }
            }
            else
            {

                if (www.result == UnityWebRequest.Result.ConnectionError)
                {
                    Debug.LogError("Error de conexión: " + www.error);
                }
                else if (www.result == UnityWebRequest.Result.ProtocolError)
                {
                    Debug.LogError("Error de protocolo HTTP: " + www.error);
                }
                else
                {
                    Debug.LogError("Error desconocido: " + www.error);
                }
            }
        }
    }

    [System.Serializable]
    public class ChatResponse
    {
        public string reply;
    }

    void Start()
    {
        Debug.Log("IAManager iniciado.");
    }

    void Update()
    {
    }
}
