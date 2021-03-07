using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEditor.Animations;
using System.Threading;

 
public class Avatar : MonoBehaviour{    
 
   private static int sign_id; // property 
   public static List<int> iList = new List<int>();
   Animator animator;
    //List<int> list_num = new List<int>();
    
 
  // Create a class constructor with a parameter
  public Avatar(){    }    
 
  public void setSignId(int sign){     
      
    sign_id = sign;
      print("Mediam"+sign_id);
      iList.Add(sign_id);
      print("Listt "+iList[0]);
      
      
      //add.list_num(sign);
      
      
    }    
    // Use this for initialization
    void Start () {    
        animator = GetComponent<Animator>();
        iList.Add(0);
    }    
 
    // Update is called once per frame
    void Update () {     
       
    if(iList.Count >0){   

        
        
        System.Threading.Thread.Sleep(3000);
        
        if(animator.GetInteger("Id") != iList[0]){
            animator.SetTrigger("Trigger");

        }
             animator.SetInteger("Id",iList[0]);
        //}
        
       
      print("Slow"+iList[0]);
        iList.RemoveAt(0);
        
      
    }    else print("cococococococ"+iList.Count);
 
        
    }    
 
    
  
 
}