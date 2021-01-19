using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEditor;
using UnityEngine.Networking;

public class Upload_video : MonoBehaviour
{
    string path; 
    public RawImage rawImage;

    // Start is called before the first frame update
    public void UploadVideo ()
    {
       path = EditorUtility.OpenFilePanel("Show all images (.png)", "","png");  
      // GetImage ();
      StartCoroutine(GetTexture());
    }

    IEnumerator GetTexture () {
        UnityWebRequest www = UnityWebRequestTexture.GetTexture("file:///" + path);
        yield return www.SendWebRequest();

        if (www.isNetworkError || www.isHttpError)
        {
            Debug.Log(www.error);
        } else 
        {
            Texture MyTexture = ((DownloadHandlerTexture)www.downloadHandler).texture;
            rawImage.texture = MyTexture;
            

        }
    }

   /* public void GetImage () {
        if (path != null) {
            UpdateImage();
        }
    }
    
    public void UpdateImage () {
        WWW www = new WWW("file:///" + path");
        image.texture = www.texture;

    } */

    
}
