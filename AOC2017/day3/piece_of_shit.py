# while s < m_num:
#     if m_idx in (0,2):
#         max_sx +=1
#         counter_against = max_sx
#     else:
#         max_sy +=1
#         counter_against = max_sy
#     print(moves[m_idx],counter_against,n_size,m_idx)        
#     while n_size <= counter_against:
#         matrix[sy][sx] = s
#         sx,sy = sx + moves[m_idx][0],sy + moves[m_idx][1]
#         n_size += 1
#         s += 1
#     m_idx = (m_idx + 1) % len(moves)
#     n_size = 0
    # matrix[sy][sx] = s