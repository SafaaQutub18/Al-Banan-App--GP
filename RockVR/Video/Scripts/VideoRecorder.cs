
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
        // turn-off or turn-on the recorder
        private bool isRecord;

        // variable for recorder tool
        public Sprite enableRecord;
        public Sprite disableRecord;
        public Button button;
        
        private void Awake()
        {
            Application.runInBackground = true;
            isRecord = false;
        }

        public void startScreenRecord()
        {
            if(isRecord== true){
                isRecord = false;
                VideoCaptureCtrl.instance.StopCapture(); 
                button.image.sprite = disableRecord;      
            }        
            else{
                stopRecordAndSave();
            }
        }
         public void stopRecordAndSave()
        {
            isRecord = true;
            VideoCaptureCtrl.instance.StartCapture();
            button.image.sprite = enableRecord;
        }
}
}