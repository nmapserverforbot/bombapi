"""
Image Generator
Coded By @BiswaX
"""
import requests as req, time
from fake_useragent import UserAgent
# Package -> pip install fake-useragent

user_agent = UserAgent()


def Midjourney(prompt: str = None,
               prompt_navigate: str = None,
               model: str = "midjourney-diffusion",
               potrait: bool = False,
               scheduler: int = 0,
               sleep_timer: int = 2) -> dict:
        try:
                session = req.session()
                height, width = [768, 1024] if potrait else [512, 512]
                models = [{
                        "name": "openjourney",
                        "version":
                        '9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb',
                        "id": 'prompthero/openjourney'
                }, {
                        "name":
                        "midjourney-diffusion",
                        "id":
                        "tstramer/midjourney-diffusion",
                        "version":
                        "436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b"
                }, {
                        "name":
                        'stable-diffusion',
                        "id":
                        'stability-ai/stable-diffusion',
                        "version":
                        'db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf',
                }]
                shd = ["DDIM", "K_EULER", "PNDM", "KLMS"]
                if len(shd) + 1 < scheduler:
                        return {
                                "error":
                                f"Invalid sceheduler index choose between 0 to {len(shd) - 1}"
                        }

                m = [_ for _ in models if _['name'] == model]
                if not m:
                        return {
                                "error":
                                f"No model found with this name {model}"
                        }

                version = m[0]['version']
                mid = m[0]['id']
                url = f"https://replicate.com/api/models/{mid}/versions/{version}/predictions"
                headers = {
                        "Origin": "https://replicate.com",
                        "Referer": f"https://replicate.com/{mid}",
                        "User-Agent": user_agent.random
                }
                data = {
                        "inputs": {
                                "width": width,
                                "height": height,
                                "prompt": prompt,
                                "scheduler": shd[scheduler],
                                "num_outputs": 1,
                                "guidance_scale": 7.5,
                                "prompt_strength": 0.8,
                                "num_inference_steps": 50,
                                "negative_prompt": prompt_navigate or ""
                        }
                }
                r1 = session.post(url, json=data, headers=headers)
                uuid = r1.json().get("uuid", None)
                if not uuid:
                        return {"error": r1.text}
                while True:
                        url = f"https://replicate.com/api/models/{mid}/versions/{version}/predictions/{uuid}"
                        r2 = session.get(url)
                        _j = r2.json().get("prediction", None)
                        status = _j.get('status', None)
                        print("ID -> ", uuid)
                        print("Status -> ", status)
                        if not status:
                                return {
                                        "error": r2.text,
                                        "code": r2.status_code
                                }
                        if status == "succeeded":
                                print("Generated Successfully!")
                                return {"result": _j.get("output", None)}
                        if status in ['canceled', 'failed']:
                                return {
                                        "error":
                                        f"Image generation process: {status}",
                                        "code": r2.status_code
                                }
                        time.sleep(sleep_timer)
        except Exception as e:
                return {"error": str(e), "code": 400}


print(Midjourney("dancing cat"))
