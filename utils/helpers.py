import os


def allowed_resume(filename):
    allowed = {"pdf", "docx"}

    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed


def save_file(file, upload_folder):
    path = os.path.join(upload_folder, file.filename)
    file.save(path)
    return path