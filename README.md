<h1><img src="https://github.com/SandeepKundalwal/Post-Graduate-Project/assets/61798659/0fb6e767-b7d9-4d14-9692-a5dac7e51e96" width="45px"> &nbsp;Post Graduate Project @IIT, Mandi</h1>

<h2>Investigating User Behaviour Towards Phishing Mail Using Eye Gaze Data.</h2>
<h4>Modules:</h4>
<ul>
  <li><a href= 'https://github.com/SandeepKundalwal/Post-Graduate-Project/tree/master/Tobii%20EyeX%20Data%20Extraction'>Tobii EyeX</a>: Extracting raw data from Tobii EyeX.</li>
    <ul>
      <li>Steps to run: <br>
        - Clone the repository. <br>
        - Go to TobiiEyeDataExtraction/LocalServer, and run TobiiWeb.exe. <br>
        - Go to TobiiEyeDataExtraction/LocalClient, and click on ExtractEyeData.html.  
      </li>
    </ul>
  <li><a href= 'https://github.com/SandeepKundalwal/Post-Graduate-Project/tree/master/HeatMap%20Generation'>HeatMap Generation</a>: Generating heatmap from the raw data extracted from Tobii EyeX and superimposing it on a image to highlight the most viewed region of the image.</li>
  <ul>
      <li>Steps to run: <br>
        - Clone the repository. <br>
        - Go to HeatMapGeneration/, start terminal inside this folder and run a python server using the command <code>python -m http.server 8000</code>. <br>
        - open browser and go to http://localhost:8000/
        - click on GenerateHeatMap.html.  
      </li>
    </ul>
</ul>
