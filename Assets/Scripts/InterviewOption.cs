using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement; // Cargar escenas.

public class InterviewOption : MonoBehaviour
{
    // Estas funciones se llamarán cuando se haga clic en el respectivo botón

    private void entrevistaDesarrollador()
    {
        // Cambia a la escena especificada cuando el objeto es clicado
         SceneManager.LoadScene("InterviewAccount"); //Cambio de escena apra desarrolladores(Programadores)
    }
    public void entrevistaContador()
    {
        SceneManager.LoadScene("InterviewAccount"); // Cambio de escena para contadores
    }
    public void entrevistaPsicologo()
    {
        SceneManager.LoadScene("InterviewAccount"); // Cambio de escena para psicologos
    }
    public void ExitGame()
    {
        #if UNITY_EDITOR
            UnityEditor.EditorApplication.isPlaying = false;
        #else
            Application.Quit();
        #endif
    }
}
