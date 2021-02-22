
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Avatar : MonoBehaviour{

   private static int sign_id; // property 
   Animator animator;

  // Create a class constructor with a parameter
  public Avatar(){}

  public void setSignId(int sign){      
    sign_id = sign;
    }
    // Use this for initialization
    void Start () {
        animator = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update () {   
        representSign();  
    }

    public void representSign(){
    animator.SetInteger("Id", sign_id);
    }

}
