is_registered = True
email_verified = True
phone_verified = False

account_active = is_registered and (email_verified or phone_verified)

print("Registered:", is_registered)
print("Email verified:", email_verified)
print("Phone verified:", phone_verified)
print("Account active:", account_active)
