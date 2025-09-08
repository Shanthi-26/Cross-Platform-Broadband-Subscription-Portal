import streamlit as st
from datetime import datetime, timedelta
from db import update_subscription_expiry, cancel_subscription

def renew_subscription(sub_id, current_expiry, days=30):
    if current_expiry and current_expiry > datetime.now():
        new_expiry = current_expiry + timedelta(days=days)
    else:
        new_expiry = datetime.now() + timedelta(days=days)
    update_subscription_expiry(sub_id, new_expiry)
    st.success(f"Subscription renewed till {new_expiry.strftime('%Y-%m-%d')}")

def cancel_sub(sub_id):
    cancel_subscription(sub_id)
    st.success("Subscription cancelled.")
