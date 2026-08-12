#Character level chunking
# def chunk_text(text, chunk_size=500, overlap=50):
#     chunks = []

#     start = 0

#     while start < len(text):
#         end = start + chunk_size

#         chunk = text[start:end]
#         chunks.append(chunk)

#         start = end - overlap

#     return chunks


#============================================================================================


#Word aware chunking
# def chunk_text(text, chunk_size=500, overlap=50):
#     chunks = []
#     start = 0
#     text_length = len(text)

#     while start < text_length:

#         end = min(start + chunk_size, text_length)

#         # Avoid cutting at the end in the middle of a word
#         if end < text_length:
#             last_space = text.rfind(" ", start, end)

#             if last_space != -1 and last_space > start:
#                 end = last_space

#         chunk = text[start:end].strip()

#         if chunk:
#             chunks.append(chunk)

#         # Stop if we reached the end
#         if end >= text_length:
#             break

#         # Create overlap
#         start = end - overlap

#         # Avoid starting the next chunk in the middle of a word
#         next_space = text.find(" ", start)

#         if next_space != -1:
#             start = next_space + 1

#     return chunks


#=========================================================================================


#sentence aware chunking
# def chunk_text(text, chunk_size=500, overlap=50):
#     chunks = []
#     start = 0
#     text_length = len(text)

#     while start < text_length:

#         # Target end position
#         end = min(start + chunk_size, text_length)

#         # Find a meaningful boundary
#         if end < text_length:

#             # 1. Prefer paragraph boundary
#             paragraph_end = text.rfind("\n\n", start, end)

#             if paragraph_end > start:
#                 end = paragraph_end

#             else:
#                 # 2. Prefer sentence boundary
#                 sentence_end = max(
#                     text.rfind(".", start, end),
#                     text.rfind("?", start, end),
#                     text.rfind("!", start, end)
#                 )

#                 if sentence_end > start:
#                     end = sentence_end + 1

#                 else:
#                     # 3. Fall back to word boundary
#                     word_end = text.rfind(" ", start, end)

#                     if word_end > start:
#                         end = word_end

#         # Extract chunk
#         chunk = text[start:end].strip()

#         if chunk:
#             chunks.append(chunk)

#         # Stop if we reached the end
#         if end >= text_length:
#             break

#         # Calculate next start using overlap
#         next_start = end - overlap

#         # Safety: next start MUST move forward
#         if next_start <= start:
#             next_start = end

#         # Move to next word boundary if possible
#         next_space = text.find(" ", next_start)

#         if next_space != -1:
#             start = next_space + 1
#         else:
#             start = end

#     return chunks


#================================================================================

#cleaner approach of sentence aware without overlap = Split the text where a sentence ends (., !, or ?) followed by whitespace.
# import re

# def chunk_text(text, chunk_size=500, overlap=50):
#     chunks = []

#     # Split text into sentences
#     sentences = re.split(r'(?<=[.!?])\s+', text)

#     current_chunk = ""

#     for sentence in sentences:

#         # Check whether adding this sentence exceeds chunk size
#         if len(current_chunk) + len(sentence) + 1 <= chunk_size:
#             current_chunk += sentence + " "

#         else:
#             # Save the current chunk
#             if current_chunk:
#                 chunks.append(current_chunk.strip())

#             # Start a new chunk
#             current_chunk = sentence + " "

#     # Add the final chunk
#     if current_chunk:
#         chunks.append(current_chunk.strip())

#     return chunks


#===============================================================================


#cleaner approach of sentence aware with overlap
import re

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []

    # Split text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    current_chunk = []
    current_length = 0

    for sentence in sentences:
        sentence = sentence.strip()

        if not sentence:
            continue

        sentence_length = len(sentence) + 1

        # If adding this sentence exceeds the chunk size
        if current_chunk and current_length + sentence_length > chunk_size:

            # Save the current chunk
            chunks.append(" ".join(current_chunk))

            # Create overlap using complete sentences
            overlap_sentences = []
            overlap_length = 0

            # Start from the last sentence and move backwards
            for previous_sentence in reversed(current_chunk):
                overlap_sentences.insert(0, previous_sentence)
                overlap_length += len(previous_sentence) + 1

                if overlap_length >= overlap:
                    break

            # Start the new chunk with overlap
            current_chunk = overlap_sentences
            current_length = sum(
                len(sentence) + 1
                for sentence in current_chunk
            )

        # Add the current sentence
        current_chunk.append(sentence)
        current_length += sentence_length

    # Add the final chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
