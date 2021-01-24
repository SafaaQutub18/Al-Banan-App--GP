using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEditor;
//using UnityEngine.Networking;

public class Upload_video : MonoBehaviour
{
    string path; 
    public RawImage rawImage;

    // Start is called before the first frame update
    public void UploadVideo ()
    {
       path = EditorUtility.OpenFilePanel("Show all images (.png)", "","png");  
      GetImage ();
    }

      public void GetImage () {
        if (path != null) {
            UpdateImage();
        }
    }
    
    public void UpdateImage () {
        WWW www = new WWW("file:///" + path);
        rawImage.texture = www.texture;

    } 

    
}
