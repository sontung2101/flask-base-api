from helpers import codes

ERROR_CODE = {
    codes.UNEXPECTED_EXCEPTION: codes.UNEXPECTED_EXCEPTION,
    codes.AUTHENTICATION_FAILED: codes.UNEXPECTED_EXCEPTION,
    codes.PERMISSION_DENIED: codes.PERMISSION_DENIED,
    codes.VALIDATION_ERROR: codes.VALIDATION_ERROR,
    codes.ALREADY_EXITED: codes.ALREADY_EXITED,
    codes.DOES_NOT_EXIST: codes.DOES_NOT_EXIST,
}

ERROR_MESSAGE = {
    codes.UNEXPECTED_EXCEPTION: "Unexpected Exception.",
    codes.AUTHENTICATION_FAILED: "Authentication failed.",
    codes.PERMISSION_DENIED: "Permission denied.",
    codes.VALIDATION_ERROR: "Validation error.",
    codes.ALREADY_EXITED: "Already exited.",
    codes.DOES_NOT_EXIST: "Does not exist",

}
