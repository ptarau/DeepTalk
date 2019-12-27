import os
from deep_talk.qpro import *

def ptest():
  f = 'examples/bfr'
  qf = f + '_query.pro'
  gm = export_to_prolog(f)
  prolog = Prolog()
  prolog.consult(f + '.pro')
  q = prolog.query('listing(dep)')
  next(q)
  q.close()
  qgm = GraphMaker(params=params)
  query_to_prolog('What is the BFR?', gm, qgm, f)
  prolog.consult(qf)
  q = prolog.query('listing(query_sent)')
  next(q)
  q.close()


def q0():
  d=txt_quest('examples', 'tesla', 'tesla_quest')
  print('LOG',d)


def q1():
  d=txt_quest('examples', 'bfr', 'bfr_quest')
  print('LOG',d)



def t0():
  dialog_about('examples/tesla',
               "How I have a flat tire repaired?")


def t0a():
  dialog_about('examples/tesla',
      "How I have a flat tire repaired?  \
      Do I have Autopilot enabled? \
      How I navigate to work? \
      Should I check tire pressures?")


def t1():
  d=dialog_about('examples/bfr',
               "What space vehicles SpaceX develops?")
  print('Sentence IDs: ',d)


def t2():
  # dialog_about('examples/bfr')
  dialog_about('examples/hindenburg',
               "When did the  fire start on the Hindenburg?")


def t3():
  dialog_about('examples/const',
  # "How many votes are needed for the impeachment of a President?"
        'How can a President be removed from office?'
  )


def t4():
  dialog_about('examples/summary',
               "How we obtain summaries and keywords from dependency graphs?")


def t5():
  dialog_about('examples/heaven',
               "What does the Pope think about heaven?")


def t6():
  dialog_about('examples/einstein',
               "What does quantum theory tell us about our \
                description of reality for an observer?")


def t7():
  dialog_about('examples/kafka',
               # "What does the doorkeeper say about entering?"
               "Why does K. want access to the law at any price?"
               )


def t8():
  dialog_about('examples/test',
               "Does Mary have a book?")


def t9():
  dialog_about('examples/relativity',
               "What happens to light in the presence of gravitational fields?")


def t10():
  pdf_chat_with('pdfs', 'textrank',
                about='What are the applications of TextRank? \
      How sentence extraction works? What is the role of PageRank?')


def all_ts():
  for i in range(0, 10):
    f = 't' + str(i)
    eval(f + "()")
