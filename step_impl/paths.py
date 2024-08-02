import step_impl.urls as url

paths = {
    url.login: {
        "username_input": "user_name_id",
        "password_input": "password_input_id",
        "login_button" : "login_button_id"
    },
    url.home:{
        "menu_transfer": "menu_transfer_id"
    },
    url.trasfer:{
        "balance_input": "balance_input_id",
        "non_campaign_bank_selector": "non_campaign_bank_selector_id",
        "transfer_amount_input": "transfer_amount_input_id",
        "recipient_name_input": "recipient_name_input_id",
        "complete_transfer_button": "complete_transfer_button_id",
        "balance_input":"balance_input_id"
    }
}
