class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    CLIENT_SECRET = "SHt8Q~MikbPio2T.RL2VcwRHPsQrICztLLlZua89" 
    TENANT_ID = "2605f990-81ed-4ce6-adfb-8167db5a8a09"
    # AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
    AUTHORITY = "https://login.microsoftonline.com/" + TENANT_ID  # For multi-tenant app
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"
    CLIENT_ID = "f306f67f-09e0-45db-9ee5-f5005c1808e7"
    #   Note that this will be the end of the URI entered back in Azure AD
    REDIRECT_PATH = "/token"  # Used to form an absolute URL, 
        # which must match your app's redirect_uri set in AAD
    LOGOUT_URI = "https://localhost:5555/login"
    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session