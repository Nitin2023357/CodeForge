function Layout({
  leftPanel,
  rightPanel
}) {
  return (
    <div
      style={{
        display: "flex",
        gap: "20px"
      }}
    >
      {leftPanel}
      {rightPanel}
    </div>
  );
}

export default Layout;