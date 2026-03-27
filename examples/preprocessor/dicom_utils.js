import { readDicomTags, readImageDicomFileSeries } from "https://cdn.jsdelivr.net/npm/@itk-wasm/dicom@7.6.4/dist/bundle/index-worker-embedded.min.js";
import { writeImage } from "https://cdn.jsdelivr.net/npm/@itk-wasm/image-io@1.6.1/dist/bundle/index-worker-embedded.min.js";;


const PATIENT_NAME_TAG = "0010|0010";
const SERIE_DESCRIPTION_TAG = "0008|103e";

const EXIT_SUCCESS = true
const EXIT_FAILURE = false

// Notice the patient_name destructuring which match the inputs param to the widget on the python side
export async function validateDicomFilePatientName(dicom_file, { patient_name }) {
    console.log({dicom_file});
    const options = {
        tagsToRead: { tags: [SERIE_DESCRIPTION_TAG, PATIENT_NAME_TAG] }
    }

    const { tags } = await readDicomTags(dicom_file, options);
    console.log({ tags })

    for (const [tag_code, tag_value] of tags) {
        if (tag_code === PATIENT_NAME_TAG) {
            if (tag_value !== patient_name && tag_value !== "Anonymized") {
                const output = {
                    expected: patient_name,
                    got: tag_value
                };
                return {
                    status: EXIT_FAILURE,
                    outputs: [output]
                };
            }
        }
    }

    return {
        status: EXIT_SUCCESS,
        outputs: [
            dicom_file
        ]
    }
}


export async function generateNIFTIFromDicomFileSet(dicom_fileset, { output_file_name }) {
    console.log(dicom_fileset);
    const inputs = await Promise.all(
      dicom_fileset.map(async (file) => {
        const buffer = await file.arrayBuffer();
        return {
          path: file.name,
          data: new Uint8Array(buffer),
        };
      })
    );

    let image_result;
    try {
        image_result = await readImageDicomFileSeries({ inputImages: inputs, singleSortedSeries: true });
    } catch (e) {
        return {
            status: false,
            outputs: "Error while reading DICOM file series"
        }
    }

    const nifti_image_result = await writeImage(
      image_result.outputImage,
      output_file_name,
      { mimeType: "image/nii" }
    );

    const blob = new Blob([nifti_image_result.serializedImage.data.buffer]); 

    return { 
        status: true,
        outputs: [new File([blob], output_file_name)],
    }
}
