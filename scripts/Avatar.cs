
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

 
   private int sign_id // property
  { get; set; }

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




    void OnCollisionEnter(Collision col) {
        if (col.gameObject.CompareTag("Enemy"))
        {
            animator.SetTrigger("Die");
        }
    }

}
