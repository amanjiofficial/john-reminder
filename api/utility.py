def struct_msg(status="", msg=""):
    """
    JSON message structure
    Args:
        status: status (ok, failed)
        msg: the message content
    Returns:
        JSON message
    """
    return {
        "status": status,
        "msg": msg
    }
