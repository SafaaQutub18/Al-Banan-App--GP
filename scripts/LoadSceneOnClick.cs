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
    public GameObject text_running;
    private GameObject translate_error;


void Start()
	{  
		//StartCoroutine(displayTranslatedVideos());
}
    public void LoadScene(string sceneName)
    {

    text_running= GameObject.Find("running_translate_text");
    translate_error = GameObject.Find("translate_error massage");
    Debug.Log(text_running.GetComponent<Text>().text);
    if(text_running.GetComponent<Text>().text == "false" ){
        SceneManager.LoadScene(sceneName);
        }

    if (text_running.GetComponent<Text>().text == "true")
        //أنقر زر إيقاف الترجمة أولا
        translate_error.GetComponent<Text>().text ="ﻻﻭﺃ ﺔﻤﺟﺮﺘﻟﺍ ﻑﺎﻘﻳﺇ ﺭﺯ ﺮﻘﻧﺃ"; 

//if (text_running.text == "true")
  //  translate_error.GetComponent<Text>().text ="أنقر زر إيقاف الترجمة أولا";

        
    }

}
