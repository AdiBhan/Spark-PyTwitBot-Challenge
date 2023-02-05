<h1> <center>PyTwitBot Spark Micro-Challenge</center> <h1>

<h1>Description:</h1>
<h3>Join the PyTwitBot Challenge and showcase your Python skills by creating a unique Twitter bot! Utilize the power of the Python programming language and Twitter API to automate tweets, interact with users, and bring your bot to life. Show off your creativity and impress the community with your bot's functionality. Are you up for the challenge?<h3>
<br>
<h3><b>Prequistes:</b>
<ul>
    <li> Have a <b><i>verified</i></b> twitter account.  </li>
       <ul> <li><i><b>IMPORTANT:</b> You will not be able to complete these steps without verifying your twitter account. Go to Your Account -> Account Information -> Phone Number, and make sure it's verified. </i></li></ul>
   <li> Have access to an IDE (preferrably VSCode, but any IDE that supports
python should work). In this challenge, I will assume you will be using VSCode, if you don't have it installed you can download it <a href = "https://code.visualstudio.com/download"><b>here</b></a>. </li>
    <li> Have a desire to create/build something cool!</li><ul></h3>
<br>

<h1> STEP 1 - Setup</h1>

<h3>

To start, we must first install the Tweepy Module

1. Install <b><a href= "https://docs.tweepy.org/en/stable/">Tweepy</a></b>. This library will allow us to use Twitter API and allow us to automate posting tweets, likes, etc. Open up VSCode.
   <ul><li>To install, open up a new terminal in VSCode (or type Ctrl-T if on Windows), and type in the terminal "pip install tweepy" </li></ul>

2. Creating a Twitter developer account
<ul><ul><li> Head over to the <a href = "https://developer.twitter.com"><b>Twitter Developer Portal</b></a> and follow along with the pictures </li></ul></ul>

<img src = "https://i.gyazo.com/634d1cd9f2424b7a1ce562aec6afaf47.jpg" > </img>
<img src = "https://i.gyazo.com/fa9e95640959d44609d0dde3249971a2.png" > </img>
<img src = "https://i.gyazo.com/5ec367c21b4ccde53692b9769834bbd2.png" > </img>

<img src = "https://i.gyazo.com/789b743fc9146701c2ff11f1eaafe8fd.png" > <img>
<br>

<center>If you have reached this step correctly, you will be prompted to verify your developer account. If you are having any issues reaching this step feel free to email me at abhan03@bu.edu or ask a Spark Ambassador for help.</center><br>

<img src = "https://i.gyazo.com/06aec855ab344e6ef77c2de298fde1fd.png" > <img>
<img src = "https://i.gyazo.com/acafb451593b85bec42f8024ec1aa39e.png"> </img>

<center>You should see three different keys. Copy them and place them under the appropiate headings in your settings.py file. These keys will be used to authenticate your account</ul>

 <ul> 
 <h3> <b>Side Note</b></h3>
 1. It's important you keep these safe and secret (or anyone else can access your app, which we don't want)<br>
 2. Don't worry, if you forget them or lose them there is a way to re-generate them as well.</center><br></ul>
<ul><center>
<h1 >How To Regenerate Keys (Optional)</h1>
<h3> If you lost for your keys or want to regenerate, follow along, otherwise you can skip this step.
</h3><h3> Head over to <a href = "https://developer.twitter.com/en/portal/dashboard"> https://developer.twitter.com/en/portal/dashboard<a></h3></h3></center>
<img src = "https://i.gyazo.com/a6dc4bd694f9415bb26cb432db490571.png"></img>
 <img src  = "https://i.gyazo.com/712da604a57dd025b56854d00f670f2f.png"> </img></ul>
</h3></a>
<br></br>

<h1> <center>Applying for Elevated Access</center></h1>
<ul><li>
<h3>Go to  <a href = "https://developer.twitter.com/en/portal/dashboard"> 
https://developer.twitter.com/en/portal/dashboard</a> and under the "Products" section click on Twitter API v2. </li><li>
</h3><h3>Click the apply"Apply" and fill out the form. You will be asked some basics questions, i.e "Why will you use TwitterAPI for?". Getting this access will allow us to give our bot more functionality</h3></li></ul><br></br></li>

<h1> <center>Setting up Authentication</center></h1>
<ul><li>
<h3>Go to  <a href = "https://developer.twitter.com/en/portal/dashboard"> 
https://developer.twitter.com/en/portal/dashboard</a> and under "Project 1", you should see the name of your project. Click on it, and  follow along with the pictures. </ul></li>

<img src = "https://i.gyazo.com/97c10305dc091053a696f89b4b648714.png"></img>

<img src = "https://i.gyazo.com/9330a72fe27026d440b6a197e67d48a1.png"> </img>

</h3><h3>You can skip the rest of the input boxes as they are optional. Click the black "Save" button at the very bottom</h3><br></br>

</h3>
<h1>STEP 2 -  Programming the bot & template.py File</h1>
 <br><center>
<h3> If you want to make your bot more advanced and see a full set of all the functionality you can 
give to your bot,<a href = "https://docs.tweepy.org/en/stable/"> https://docs.tweepy.org/en/stable/ </a> is your best friend.
</center>
<br><h3><ul><li>
 I created a basic template called "template.py" that will tweet "My first automated Tweet! #SparkFun #Python #Tweepy" when you run the python file. I suggest you use it as a basis and mess around with the file and add features from there.
</li>
<br>
<li>
 I also included a previous project I made with tweepy and some external apis when first learning Python. When the file is run, it will find the highest and lowest temperatures every hour from a list of over 100 U.S cities, and tweet them out.
</h3></li>
</ul>
