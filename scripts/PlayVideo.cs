using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Video;
using UnityEditor;

<<<<<<< HEAD

=======
// HI
>>>>>>> 247b421c982b46ff6b2c5de75b3dfd133404025c
//using UnityEngine.Networking;

public class PlayVideo : MonoBehaviour
{


    public GameObject playIcon;

    // path of recoded video
    public static string path; 
    public GameObject get_path;

    // play of recoded video in list 
     public void playVideo(){ 
		path= get_path.GetComponent<Text>().text;

        // disply video in defulte movie player
        System.Diagnostics.Process.Start(path);

    }


}

