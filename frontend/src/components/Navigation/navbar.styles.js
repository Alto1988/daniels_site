import styled from "styled-components";

const NavbarStyles = styled.nav`
  background-color: #fff;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 15px;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  z-index: 100;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.08);
  .li Link {
    font-style: italic;
  }
`;
export default NavbarStyles;
