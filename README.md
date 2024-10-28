![alt text](<images/twilio-microservice.drawio.png>)
### 1. Create Lambda Function
I use Python 3.12.7 for this project.

1. Sign-in to https://aws.amazon.com/console/
2. Navigate to `Lambda` > `Create function`
![alt text](<images/image.png>)
3. Copy and past the code from `send-sms.py`

### 2. Get Account SID and Authentication Token from Twilio
I bought a number from Twilio and load a few dollars.

1. Login to your twilio account.
2. Under Account Dashboard, Note Account SID and Auth Token.
3. Under Active Numbers, note the purchase number down.

### 3. Setup SID and Token as Environment Variables
1. Navigate to Lambda function that just created.
2. Configuration > Environment Variables.
![alt text](<images/image-1.png>)

### 4. Setup Layer
My python code will need Twilio library in order to run. This step will require pip and 7zip.

1. On local computer, create a virtual environment and name it `env`.
```
python -m venv env
```

2. `Activate` the virtual environment.
```.env/Scripts/Activate```

3. Install twilio and export it into `requirements.txt`.
```
pip install twilio
pip freeze > requirements.txt
```

4. `Deactivate` virtual envrinment.
```Deactivate```

5. Create a new folder and name it `Python`.
```mkdir -p python```

6. Install packages to this folder.
```pip install -r requirements.txt --target python```

7. Zip `python` folder to `python.zip`.
```7z a -tzip python.zip python```

8. Navigate to `AWS Lambda console` > `Layers` > `Create layer` > Upload the zip file.
![alt text](<images/image-2.png>)

### 5. Assign Layer to Lambda Function

1. Navigate to our `send-sms1` function.
2. Under `Code` > `Layers` > assign layer that we have just created.

### 6. Setup API Gateway

1. Create a Regional `REST API`.
2. Create a Resource and give it a name.
3. Create `Post` method and point it to our lambda function.

### 7. Setup Custom domain names
A registered domain and valid ACM certificate are required for this step. I will use my subdomain for this API custom domain.

1. Under `API Gateway` > `Custom domain names` > `Add domain name`
![alt text](<images/image-3.png>)
2. Under `Route 53` > create an `A Record` pointing to the `Custom Domain Name API`
![alt text](<images/image-4.png>)