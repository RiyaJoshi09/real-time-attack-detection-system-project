import React from 'react';
import { Alert } from '@mui/material';

export default function AlertBanner({ message }) {
  if (!message) return null;
  return (
    <Alert severity="error" sx={{ my: 2 }}>
      🚨 Attack Detected: {message}
    </Alert>
  );
}
