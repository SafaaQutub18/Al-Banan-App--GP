using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;


public class start_button : MonoBehaviour
{
    // Start is called before the first frame update
    public void StartApp()
    {
       //Application.LoadLevel(scene_name);
       UnityEngine.SceneManagement.SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex +1);

    }//Linahhhhhhh

}
