using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Video;
using UnityEditor;


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

