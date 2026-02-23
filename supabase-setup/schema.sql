-- ============================================================
-- Supabase Setup for personal-website-finals
-- Run this in your Supabase SQL Editor
-- ============================================================

-- Create the comments table
CREATE TABLE IF NOT EXISTS comments (
  id         uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  name       text NOT NULL CHECK (char_length(name) <= 100),
  message    text NOT NULL CHECK (char_length(message) <= 1000),
  created_at timestamptz DEFAULT now() NOT NULL
);

-- Enable Row Level Security
ALTER TABLE comments ENABLE ROW LEVEL SECURITY;

-- Allow anyone to READ comments (public guestbook)
CREATE POLICY "Allow public read"
  ON comments FOR SELECT
  TO anon
  USING (true);

-- Allow anyone to INSERT comments (public guestbook)
CREATE POLICY "Allow public insert"
  ON comments FOR INSERT
  TO anon
  WITH CHECK (true);

-- Index for faster ordering by date
CREATE INDEX IF NOT EXISTS comments_created_at_idx ON comments (created_at DESC);

-- ============================================================
-- Seed some sample data (optional - delete before production)
-- ============================================================
INSERT INTO comments (name, message) VALUES
  ('Prof. Sample', 'Great portfolio! Clean and professional.'),
  ('Classmate Test', 'Love the space aesthetic — very you!'),
  ('IT Department', 'Excellent technical implementation. Well done!');
