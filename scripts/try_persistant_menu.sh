curl -X POST -H "Content-Type: application/json" -d '{
"get_started":{
    "payload":"action@getStarted"
}
}' "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAAFsSgu9R1IBAB3Y8e3NDdE9VqIPsmyiMWCrXuJADaW5WOJytb6LoepS6elRKSpZAZBNna0sFpFZCkC4yv8S35m3lwZAnIDibMAzZAay1sk7vr02wGwx5wgnbC48y8BmpnBvE4AU6iHv8YCPHvE28xIpAjnqEcuEnwJLtAR4q8AZDZD"


curl -X POST -H "Content-Type: application/json" -d '{
"persistent_menu":[
    {
    "locale":"default",
    "composer_input_disabled":true,
    "call_to_actions":[
        {
        "title":"Info",
        "type":"nested",
        "call_to_actions":[
            {
            "title":"Help",
            "type":"postback",
            "payload":"SUGGESTIONS"
            },
            {
            "title":"Contact Me",
            "type":"postback",
            "payload":"CONTACT_INFO_PAYLOAD"
            }
        ]
        },
        {
        "type":"web_url",
        "title":"Visit website ",
        "url":"http://www.techiediaries.com",
        "webview_height_ratio":"full"
        }
    ]
    },
    {
    "locale":"zh_CN",
    "composer_input_disabled":false
    }
]
}' "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAAFsSgu9R1IBAB3Y8e3NDdE9VqIPsmyiMWCrXuJADaW5WOJytb6LoepS6elRKSpZAZBNna0sFpFZCkC4yv8S35m3lwZAnIDibMAzZAay1sk7vr02wGwx5wgnbC48y8BmpnBvE4AU6iHv8YCPHvE28xIpAjnqEcuEnwJLtAR4q8AZDZD"
