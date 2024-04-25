# WhatsAppBotForFieldTeamHelper

Simple API for responding to WhatsApp automation requests

1. create the virtual environment
```ps
python -m venv .venv
```

2. activate the virtual environment
```ps
.\.venv\Scripts\Activate
```

3. install development dependencies
```ps
pip install -r requirements.txt
```

4. run the development environment
```ps
uvicorn main:app --host 0.0.0.0 --port 8888 --reload
```

5. on an Android phone, install the [Automate](https://llamalab.com/automate/) app by [clicking here](https://play.google.com/store/apps/details?id=com.llamalab.automate)

6. connect the smartphone to the same network as the API server

7. launch WhatsApp automation script
