using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEditor.Animations;
using System.Threading;

 
public class Avatar : MonoBehaviour{    

   // list for storing the signs of the words  
   public static List<int> list_signId = new List<int>();
   // declere object
   Animator animator;
    
  // Create a class constructor
  public Avatar(){    }    
  
  public void setSignId(int sign_id){  
     //add sign id to list  
     list_signId.Add(sign_id);    
    }    

    // Use this function for initialization
    void Start () { 
      //initialize the animator object
      animator = GetComponent<Animator>();

      // invoke representSign function every 2.5 sec
      InvokeRepeating("representSign", 0.0f, 2.5f);
    }    
 
    void representSign () {   

      //check if there are signs in the list  
      if(list_signId.Count >0){  

        // stop reapeting of sign
        animator.SetTrigger("Trigger");

        //set the avatar animator parameter(Id)
        animator.SetInteger("Id",list_signId[0]);
        print("sign id"+list_signId[0]);
        
        //remove the represented sign from the list
        list_signId.RemoveAt(0);   
     }      
    }    
 
    
  
 
}