
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
        public Sprite enableRecord;
        public Sprite disableRecord;
        public Button button;
        
        private bool isRecord;
        private void Awake()
        {
            Application.runInBackground = true;
            isRecord = false;
        }

        public void Start_StopScreenRecord()
        {
            if(isRecord== true){
                isRecord = false;
                VideoCaptureCtrl.instance.StopCapture(); 
                button.image.sprite = disableRecord;      
            }        
            else{
                isRecord = true;
                VideoCaptureCtrl.instance.StartCapture();
                button.image.sprite = enableRecord;
               
            }
            
                    
             
    }
}
}