import React from 'react';
import { Box, Typography } from '@mui/material';

export default function Footer() {
  return (
    <Box sx={{ textAlign: 'center', p: 2, mt: 4, bgcolor: 'background.paper' }}>
      <Typography variant="body2" color="textSecondary">
        &copy; {new Date().getFullYear()} Real-Time Attack Detection System
      </Typography>
    </Box>
  );
}
