function UploadBox({
  uploadPDF,
  filename,
  uploaded,
  loading
}) {
  const handleChange = (event) => {

    const file = event.target.files[0];

    if (!file) return;

    if (file.type !== "application/pdf") {

      alert("Please select a PDF file");

      return;
    }

    uploadPDF(file);
  };


  return (

    <div className="upload-box">

      <h2>
        Upload Study Material
      </h2>

      <p>
        Upload your lecture notes or textbook PDF.
      </p>

      <label className="upload-button">

        {loading
          ? "Processing..."
          : "Choose PDF"
        }

        <input
          type="file"
          accept=".pdf"
          onChange={handleChange}
          hidden
        />

      </label>


      {uploaded && (

        <p className="filename">

          ✓ {filename}

        </p>

      )}

    </div>
  );
}

export default UploadBox;