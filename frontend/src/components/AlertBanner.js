import React from 'react';
import { Alert, Collapse } from '@mui/material';

const AlertBanner = ({ log, open }) => {
  return (
    <Collapse in={open}>
      <Alert severity="error">
        🚨 Attack detected from IP: <strong>{log?.ip}</strong> — Payload contains suspicious pattern(s)!
      </Alert>
    </Collapse>
  );
};

export default AlertBanner;