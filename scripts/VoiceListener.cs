using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;
using UnityEngine.UI;
using System.Threading;
using System;


public class VoiceListener : MonoBehaviour{

    public Sprite enableListen;
    public Sprite disableListen;
    public Button button;

    Thread mThread;
    public string connectionIP = "127.0.0.1";
    public int connectionPort = 25001;
    IPAddress localAdd;
    TcpListener listener;
    TcpClient client;
    

    // varible to control the activation 
    string isListening = "false";
    private GameObject translate_error;
    private GameObject translate_button;
    private GameObject translate_button_text;

    //public GameObject translation_bt;
    private GameObject text_isListening;


    //function activated by the user to start or stop the translation
    public void startStopListening(){ 

        // bring the values from unity to deal with exeptions
        text_isListening = GameObject.Find("isListening_text");
        translate_button = GameObject.Find("TranslateButton");
        translate_button_text = translate_button.transform.Find("TranslateText").gameObject;
        translate_error = GameObject.Find("error_massage");


        //check if the translation is activated to stop it.
        if(isListening.Equals("true")) {
        isListening = "false";

        //send the isListening value to unity
		text_isListening.GetComponent<Text>().text ="false";
        // delete error massage
        
        translate_error.GetComponent<Text>().text =""; 

        // change the value of translate_button as بدء الترجمة
        translate_button_text.GetComponent<Text>().text ="ﺔﻤﺟﺮﺘﻟﺍ ﺀﺪﺑ";

        listener.Stop();
        Debug.Log("Stop listener");
        button.image.sprite = disableListen;
       // VideoCaptureCtrl.Instance.StopCapture();
        } 


        // if the translation is not activated, start it
        else {
       //socket setting
        ThreadStart ts = new ThreadStart(GetInfo);
        mThread = new Thread(ts);
        mThread.Start();

        //send the isListening value to unity 
        text_isListening.GetComponent<Text>().text ="true";

        //change the text of the translate button.
        translate_button_text.GetComponent<Text>().text ="ﺔﻤﺟﺮﺘﻟﺍ ﻑﺎﻘﻳﺇ";
		//change the icon of listening
        button.image.sprite = enableListen;
        
        } 
    }

    void GetInfo(){
        localAdd = IPAddress.Parse(connectionIP);
        listener = new TcpListener(IPAddress.Any, connectionPort);
        listener.Start();
        Debug.Log("Start listener");
        client = listener.AcceptTcpClient();
        isListening = "true";

       

        while (isListening.Equals("true")){
            SendAndReceiveData();
        }
    }
    void SendAndReceiveData(){ 
        NetworkStream nwStream = client.GetStream();
        //---receiving Data from the Host----
        byte[] buffer = new byte[client.ReceiveBufferSize];
        int bytesRead = nwStream.Read(buffer, 0, client.ReceiveBufferSize); //Getting data in Bytes from Python
        string dataReceived = Encoding.UTF8.GetString(buffer, 0, bytesRead); //Converting byte data to string
        
        // initialize avatar object 
        Avatar avatar = new Avatar();

        if (dataReceived != null){
        string[] signs_id_list = dataReceived.Split(','); // split the id by comma 
        // looping throug the signs_id_list
        foreach(string sign_id in signs_id_list){
            if(!sign_id.Equals(" ")) // to prevent sign id from concatenation
            
            // convert the id from string to integer
             avatar.setSignId(Int32.Parse(sign_id));
             
        }
            
        }

    }

    }
