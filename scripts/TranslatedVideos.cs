using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEditor.Animations;
using System.Threading;
using System.IO;
using System;

public class TranslatedVideos : MonoBehaviour{   
//Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);

    string path = System.IO.Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments),"RockVR/Video");
    string[] files = System.IO.Directory.GetFiles( "path" );

    public void displayVideos(){  
       print(path);
    }
    
        

}