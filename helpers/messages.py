from helpers import codes

ERROR_CODE = {
    codes.UNEXPECTED_EXCEPTION: codes.UNEXPECTED_EXCEPTION,
    codes.AUTHENTICATION_FAILED: codes.UNEXPECTED_EXCEPTION,
    codes.PERMISSION_DENIED: codes.PERMISSION_DENIED,
    codes.VALIDATION_ERROR: codes.VALIDATION_ERROR,
    codes.ALREADY_EXITED: codes.ALREADY_EXITED,
    codes.DOES_NOT_EXIST: codes.DOES_NOT_EXIST,
    codes.NOT_A_VALID_EMAIL_ADDRESS: codes.NOT_A_VALID_EMAIL_ADDRESS,
    codes.EXTENSIONS_NOT_ALLOWED: codes.EXTENSIONS_NOT_ALLOWED,
    codes.NO_FILE_PART: codes.NO_FILE_PART,
    codes.NO_FILE_SELECTED: codes.NO_FILE_SELECTED,
    codes.NO_INPUT_DATA: codes.NO_INPUT_DATA,
}

ERROR_MESSAGE = {
    codes.UNEXPECTED_EXCEPTION: "Unexpected Exception.",
    codes.AUTHENTICATION_FAILED: "Authentication failed.",
    codes.PERMISSION_DENIED: "Permission denied.",
    codes.VALIDATION_ERROR: "Validation error.",
    codes.ALREADY_EXITED: "Already exited.",
    codes.DOES_NOT_EXIST: "Does not exist",
    codes.NOT_A_VALID_EMAIL_ADDRESS: "Not a valid email address.",
    codes.EXTENSIONS_NOT_ALLOWED: "Extensions not allowed",
    codes.NO_FILE_PART: "No file part in the request",
    codes.NO_FILE_SELECTED: "No file selected for uploading",
    codes.NO_INPUT_DATA: "No input data provided",

}
