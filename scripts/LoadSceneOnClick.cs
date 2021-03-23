using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using System.IO;
using System.Text;
using UnityEngine.UI;
using System;


public class LoadSceneOnClick  : MonoBehaviour {

    //public GameObject translation_bt;
    private GameObject text_isListening;
    private GameObject text_isRecord;
    private GameObject error_massage;


void Start(){ 
    // bring the values from unity to deal with exeptions
    text_isListening= GameObject.Find("isListening_text");
    text_isRecord= GameObject.Find("isRecord_Text");
    error_massage = GameObject.Find("error_massage");
    }

    public void LoadScene(string sceneName){
    
    //transfer to other scene 
    if(text_isListening.GetComponent<Text>().text == "false" && text_isRecord.GetComponent<Text>().text == "false" ){
        //error_massage.GetComponent<Text>().text ="ًﻻﻭﺃ ﻞﻴﺠﺴﺘﻟﺍ ﻑﺎﻘﻳﺇ ﺭﺯ ﺮﻘﻧﺃ";
        SceneManager.LoadScene(sceneName);
     }

    //check if listening is activated and print error massage
    if (text_isListening.GetComponent<Text>().text == "true")
        //أنقر زر إيقاف الترجمة أولا
        error_massage.GetComponent<Text>().text ="ﻻﻭﺃ ﺔﻤﺟﺮﺘﻟﺍ ﻑﺎﻘﻳﺇ ﺭﺯ ﺮﻘﻧﺃ"; 

    if (text_isRecord.GetComponent<Text>().text == "true")
        error_massage.GetComponent<Text>().text ="ًﻻﻭﺃ ﻞﻴﺠﺴﺘﻟﺍ ﻑﺎﻘﻳﺇ ﺭﺯ ﺮﻘﻧﺃ";
        
    }

     public void LoadScene_general(string sceneName){
        SceneManager.LoadScene(sceneName);
     }

}
