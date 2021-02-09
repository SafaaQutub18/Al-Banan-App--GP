using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Video;
using UnityEditor;


//using UnityEngine.Networking;

public class Upload_video : MonoBehaviour
{
    
    private VideoPlayer videoPlayer;
    private VideoSource videoSource;

    GameObject rawImage;
    public GameObject playIcon;
    private RenderTexture renderTexture;

    // path of uploded video
    public static string path; 

    private bool isPaused = false;
    private bool firstRun = true;

    // Function of upload video button
    public void UploadVideo ()
    {
       // Assign the video path selected by the user to the path variable
       path = EditorUtility.OpenFilePanel("Show all images (.mp4)", "","mp4");  
       Debug.Log("Done Uploading Video");
    }

    IEnumerator playVideo()
    { 
        playIcon.SetActive(false);
        firstRun = false;

        //Add VideoPlayer and rawImage to the GameObject
        videoPlayer = gameObject.AddComponent<VideoPlayer>();
        rawImage = GameObject.Find("RawImage");
       
        //Disable Play on Awake for both Video 
        videoPlayer.playOnAwake = false;
     
        // get Vide clip from Url
        videoPlayer.source = VideoSource.Url;
        videoPlayer.url = path;
        
        //Set video To Play 
        videoPlayer.Prepare();

        //Wait until video is prepared
        while (!videoPlayer.isPrepared)
        {
            yield return null;
        }

        Debug.Log("Done Preparing Video");
        
        //Assign the Texture from Video to RawImage to be displayed
        rawImage.GetComponent<RawImage>().texture  = videoPlayer.texture;

        //Play Video
        videoPlayer.Play();
        
        Debug.Log("Playing Video");
        while (videoPlayer.isPlaying)
        {
            Debug.LogWarning("Video Time: " + Mathf.FloorToInt((float)videoPlayer.time));
            yield return null;
        }

        Debug.Log("Done Playing Video");
    }

    public void PlayPause() {
        if(!firstRun && !isPaused) {
            videoPlayer.Pause();
            playIcon.SetActive(true);
            isPaused = true;
        } else if (!firstRun && isPaused) {
            videoPlayer.Play();
            playIcon.SetActive(false);
            isPaused = false;
        } else {
            StartCoroutine(playVideo());
        }
    }



}

