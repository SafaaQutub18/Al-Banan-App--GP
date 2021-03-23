
using System.Diagnostics;
using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;
using UnityEngine.UI;
using System.Threading;
using System;



namespace RockVR.Video.Demo
{
    public class VideoRecorder : MonoBehaviour
    {
        

        // variable for recorder tool
        public Sprite enableRecord;
        public Sprite disableRecord;
        public Button button;

        // varible to control the activation 
        private GameObject record_error;
        private GameObject record_button;
        private GameObject record_button_text;
        // turn-off or turn-on the recorder
        private bool isRecord;

        //public GameObject translation_bt;
        private GameObject text_isRecord;
        
        private void Awake()
        {
            Application.runInBackground = true;
            isRecord = false;

            // bring the values from unity to deal with exeptions
            text_isRecord = GameObject.Find("isRecord_Text");
            record_button = GameObject.Find("RecordButton");
            record_button_text = record_button.transform.Find("RecordText").gameObject;
            record_error = GameObject.Find("error_massage");
        }

        public void startScreenRecord()
        {
            if(isRecord== false){

                //send the isRecord value to unity 
                text_isRecord.GetComponent<Text>().text ="true";

                //change the text of the translate button as ايقاف التسجيل.
                record_button_text.GetComponent<Text>().text ="ﻞﻴﺠﺴﺘﻟﺍ ﻑﺎﻘﻳﺇ";

                isRecord = true;
                VideoCaptureCtrl.instance.StartCapture();
                button.image.sprite = enableRecord;     
            }        
            else{
                stopRecordAndSave();
            }
        }
         public void stopRecordAndSave()
        {
            isRecord = false;
            VideoCaptureCtrl.instance.StopCapture(); 
            button.image.sprite = disableRecord;

            //send the isRecord value to unity
            text_isRecord.GetComponent<Text>().text ="false";
            
            // delete error massage
            record_error.GetComponent<Text>().text =""; 

            // change the value of translate_button as تسجيل الترجمة
            record_button_text.GetComponent<Text>().text ="ﺔﻤﺟﺮﺘﻟﺍ ﻞﻴﺠﺴﺗ";


            
        }
}
}