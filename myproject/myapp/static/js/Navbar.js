// Navbar.js
import React from 'react';
import styled from 'styled-components';

const NavbarContainer = styled.div`
  width: 205px;
  height: 904px;
  left: 49px;
  top: 40px;
  position: absolute;
  /* Add other styles as needed */
`;

const LogoMessenger = styled.img`
  width: 60px;
  height: 60px;
  position: absolute;
  /* Add other styles as needed */
`;

// Add other Navbar components as needed

const Navbar = () => {
  return (
    <NavbarContainer>
      <LogoMessenger src="https://via.placeholder.com/60x60" />
      {/* Add other Navbar components as needed */}
    </NavbarContainer>
  );
};

export default Navbar;
