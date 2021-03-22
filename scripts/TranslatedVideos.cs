
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using System.IO;
using UnityEngine.Video;


public class TranslatedVideos : MonoBehaviour
{
	public GameObject prefab ; // This is our prefab object that will be exposed in the inspector
	public int numberToCreate; // number of objects to create. Exposed in inspector


static string  path = System.IO.Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments),"RockVR/Video");
static string[] files = System.IO.Directory.GetFiles( path );

	void Start()
	{  
		StartCoroutine(displayTranslatedVideos());
}
	void Update(){}

	private RenderTexture renderTexture;
	private VideoPlayer videoPlayer;
	private VideoSource videoSource;
	private GameObject text_path;
	private GameObject play_icon;
	private GameObject video_name;
	
  IEnumerator displayTranslatedVideos()
	{
        numberToCreate= files.Length;
		GameObject newObj ; // Create GameObject instance
		for (int i = 0; i < numberToCreate; i++)
		{			
            renderTexture = new RenderTexture(160, 100, 24);
			videoPlayer = gameObject.AddComponent<VideoPlayer>();

			 // Create new instances of our prefab until we've created as many as we specified
			newObj = (GameObject)Instantiate(prefab, transform);

			//set the file path of each video to be used in play script
			play_icon = newObj.transform.Find("PlayIcon").gameObject;
			text_path= play_icon.transform.Find("Text").gameObject;
			text_path.GetComponent<Text>().text = files[i];

			// set the name of each video
			video_name= newObj.transform.Find("VideoName").gameObject;
			video_name.GetComponent<Text>().text = files[i].Substring(files[i].IndexOf("Video")+6);  

			//Disable Play on Awake for both Video 
			videoPlayer.playOnAwake = false;
		
			// get Vide clip from Url
			videoPlayer.source = VideoSource.Url;
			videoPlayer.url = files[i] ;
			
			//Set video To Play 
			videoPlayer.Prepare();

			//Wait until video is prepared
			while (!videoPlayer.isPrepared)
			{
				yield return null;
			}
			//Assign the Texture from Video to RawImage to be displayed
				newObj.GetComponent<RawImage>().texture  =renderTexture;
				videoPlayer.renderMode = UnityEngine.Video.VideoRenderMode.RenderTexture;
       
             videoPlayer.targetTexture = renderTexture;
		
			Debug.Log(files[i]);
             
		}

	}	

}
