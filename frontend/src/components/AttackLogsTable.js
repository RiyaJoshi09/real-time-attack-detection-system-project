import React from 'react';
import {
  Table, TableBody, TableCell, TableContainer,
  TableHead, TableRow, Paper, Typography
} from '@mui/material';

export default function AttackLogTable({ logs }) {
  if (!logs || logs.length === 0) {
    return <Typography>No attacks detected yet.</Typography>;
  }

  return (
    <TableContainer component={Paper} sx={{ mt: 2 }}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Timestamp</TableCell>
            <TableCell>IP Address</TableCell>
            <TableCell>Payload</TableCell>
            <TableCell>Patterns</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {logs.map((log, idx) => (
            <TableRow key={idx}>
              <TableCell>{new Date(log.timestamp).toLocaleString()}</TableCell>
              <TableCell>{log.ip}</TableCell>
              <TableCell>{JSON.stringify(log.payload)}</TableCell>
              <TableCell>{log.patterns.join(', ')}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
