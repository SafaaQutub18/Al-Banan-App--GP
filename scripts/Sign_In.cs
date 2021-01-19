using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Sign_In : MonoBehaviour
{
    
   public void SignIn(){
       
       SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex -1 ); 

   }

    public void CreateAccountPage(){
       
       SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex +1 ); 

   }
}
