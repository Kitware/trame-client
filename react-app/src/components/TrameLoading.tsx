

export default function TrameLoading({
  message = "Loading...",
}: {
  message?: string;
}) {
  return (
    <div
      style={{
        position: "absolute",
        top: 0,
        left: 0,
        width: "100%",
        height: "100%",
        zIndex: 1000,
      }}
    >
      <div className="trame__loader" />
      <div className="trame__message">{message}</div>
    </div>
  );
}
