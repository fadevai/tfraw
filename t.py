"""
\file
\brief TensorFlow Raw library main class file
"""

#core
import os,sys;
import pprint     as pp;
import subprocess as sp;

#libs
import numpy      as np;
import tensorflow as tf;

#shortcuts
log = tf.logging.info;

"""
\brief TensorFlow Raw library main class
"""
class t: #short for tensorflow

  """
  \brief Pretty print
  """
  def pprint(Var):
    log(pp.pformat(Var,indent=2));
  #end def

  """
  \brief Halt the programme
  """
  def halt():
    os._exit(1);
  #end def

  """
  \brief Remove a TensorFlow model dir
  """
  def rm_model_dir(Model_Dir):
    try:
      Out=sp.check_output(["rm","-r",Model_Dir],stderr=sp.STDOUT);
      #if len(Out)>0:
      log(Out);
      print(Out);
    except Exception as Err:
      log(Err);
      print(Err);
    #end try    
  #end def

  """
  \brief Initialise TensorFlow
  """
  def init_ml():
    tf.logging.set_verbosity(tf.logging.INFO);    
  #end def
#end class

#export shortcuts
pprint       = t.pprint;
halt         = t.halt;
rm_model_dir = t.rm_model_dir;
init         = t.init_ml;

#end of file