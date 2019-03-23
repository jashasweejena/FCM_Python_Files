from pyfcm import FCMNotification

api_key = 'AAAA8v-tPE8:APA91bHmrFRDqZq85rPm_VXgGfIT7nbkjSSKasgUh7BBaZ68xmc2dIoCBrDk-YzLZHb12vpg1KZSaiCKywqkq7nNDqPgFn2R-wbUzlyB9J4lZZtlDSQRo8fxmuIBoopHveakFxT5qpss'
push_service = FCMNotification(api_key=api_key)
 
# OR initialize with proxies
 
proxy_dict = {
          "http"  : "http://127.0.0.1",
          "https" : "http://127.0.0.1",
        }
push_service = FCMNotification(api_key=api_key, proxy_dict=proxy_dict)
 
# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
 
registration_id = "cBb3HAeLhDw:APA91bFeBT54hH4A2hPOnPNslihrgLI8Ql4k2Js0imXEpRcK3S2VvIUwQjZXxwjjK4z1lSuFnLG1qRhtKIEchZTCozNNj0BcxBUFRepF2LddyQqOcBqHWDv-YHyLNocv2H8m4rra4D7I"
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
 
print(result)
 
# Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
# message_title = "Uber update"
# message_body = "Hope you're having fun this weekend, don't forget to check today's news"
# result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
 
# print(result)