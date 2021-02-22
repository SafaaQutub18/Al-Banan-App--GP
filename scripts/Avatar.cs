
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;



public class Avatar : MonoBehaviour
{


    Animator animator;

  

  // Create a class constructor with a parameter
  public Avatar()
  {
  
  }

 
   private static int sign_id; // property
 
    public void setSignId(int sign){
        
    sign_id = sign;

    }

 

    // Use this for initialization
    void Start () {
        animator = GetComponent<Animator>();
    }
    
    // Update is called once per frame
    void Update () {
   
          //representSign();
          
          animator.SetInteger("Id", sign_id);
    }

    public void representSign(){

  

    }



}
