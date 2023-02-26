import vtkURLExtract from "@kitware/vtk.js/Common/Core/URLExtract";

const { inject, onMounted, onBeforeUnmount } = window.Vue;

export default {
  props: {
    message: {
      type: String,
      default: "Click to reconnect...",
    },
    maxRetry: {
      type: Number,
      default: 10,
    },
    delay: {
      type: Number,
      default: 500,
    },
  },
  setup(props) {
    const trame = inject("trame");
    let interval = null;
    let retryCount = 0;

    async function connect() {
      await trame.connect();
    }

    function resetRetry() {
      if (interval) {
        clearInterval(interval);
        interval = null;
      }
    }

    onMounted(() => {
      retryCount = 0;
      const reconnect = vtkURLExtract.extractURLParameters().reconnect;
      if (reconnect) {
        console.log("reconnect", reconnect);
        if (reconnect === "auto") {
          interval = setInterval(() => {
            if (retryCount++ < props.maxRetry) {
              connect();
            } else {
              resetRetry();
            }
          }, props.delay);
        }
      }
    });

    onBeforeUnmount(() => {
      resetRetry();
    });

    return { connect };
  },
  template: `
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1000;">
      <div style="position: relative;top: 50%;left: 50%;transform: translate(-50%, -50%);-ms-transform: translate(-50%, -50%);width: 80%;text-align: center;">
        <div style="display: flex;justify-content: space-around;text-align: center;user-select: none;background-color: #f1f1f1;color: black;font-size: 16px;padding: 10px 20px;border: none;cursor: pointer;border-radius: 5px;text-align: center;width: 200px;margin: 10px auto;" @click="connect">
          <svg
            style="width: 24px"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
          >
            <path
              d="M4,1C2.89,1 2,1.89 2,3V7C2,8.11 2.89,9 4,9H1V11H13V9H10C11.11,9 12,8.11 12,7V3C12,1.89 11.11,1 10,1H4M4,3H10V7H4V3M14,13C12.89,13 12,13.89 12,15V19C12,20.11 12.89,21 14,21H11V23H23V21H20C21.11,21 22,20.11 22,19V15C22,13.89 21.11,13 20,13H14M3.88,13.46L2.46,14.88L4.59,17L2.46,19.12L3.88,20.54L6,18.41L8.12,20.54L9.54,19.12L7.41,17L9.54,14.88L8.12,13.46L6,15.59L3.88,13.46M14,15H20V19H14V15Z"
            />
          </svg>
          {{ message }}
        </div>
      </div>
    </div>
      `,
};
