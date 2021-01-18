using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class start_page : MonoBehaviour
{
    
   public void StartApp(){
       
       SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex +1 ); 

   }
}
